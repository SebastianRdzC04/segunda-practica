import os
from pymongo import MongoClient
from dotenv import load_dotenv
import json
from datetime import datetime
import glob

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "iot_database")

class MongoSession:
    def __init__(self):
        self.mongo_uri = MONGO_URI
        self.db_name = DB_NAME
        self._client = None
        self._db = None
        self.offline_dir = "offline"
        self._create_offline_dir()
        self._connect()
    
    def _create_offline_dir(self):
        """Crea la carpeta offline si no existe"""
        if not os.path.exists(self.offline_dir):
            os.makedirs(self.offline_dir)
    
    def _connect(self):
        """Conecta automáticamente a MongoDB"""
        try:
            self._client = MongoClient(self.mongo_uri, serverSelectionTimeoutMS=2000)
            self._client.server_info()
            self._db = self._client[self.db_name]
            print("✓ Conexión con MongoDB establecida exitosamente")
            return True
        except Exception as e:
            print(f"✗ Error de conexión a MongoDB: {e}")
            self._client = None
            self._db = None
            return False
    
    def exportar(self, tabla, json_data):
        """Exporta datos JSON a la tabla especificada"""
        if self._db is None:
            print("✗ Sin conexión a MongoDB. No se puede exportar.")
            self._save_offline(tabla, json_data)
            return None
            
        try:
            # Si hay conexión, primero sincronizar datos offline
            self._sync_offline_data()
            
            collection = self._db[tabla]
            result = collection.insert_one(json_data)
            print(f"✓ Datos exportados exitosamente a '{tabla}' con ID: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"✗ Error al exportar a '{tabla}': {e}")
            print("✗ No pudo exportarlo, guardando datos localmente...")
            self._save_offline(tabla, json_data)
            return None
    
    def _sync_offline_data(self):
        """Sincroniza datos offline con MongoDB cuando hay conexión"""
        if self._db is None:
            return
            
        offline_files = glob.glob(os.path.join(self.offline_dir, "*.json"))
        
        if not offline_files:
            return
            
        print(f"📤 Sincronizando {len(offline_files)} archivos offline...")
        
        for filepath in offline_files:
            try:
                # Extraer nombre de tabla del archivo
                filename = os.path.basename(filepath)
                tabla = filename.split('_')[0]  # Formato: tabla_timestamp.json
                
                # Leer datos del archivo
                with open(filepath, 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                
                # Enviar a MongoDB
                collection = self._db[tabla]
                result = collection.insert_one(json_data)
                
                # Si se envió exitosamente, eliminar archivo
                os.remove(filepath)
                print(f"✓ Sincronizado y eliminado: {filename} -> ID: {result.inserted_id}")
                
            except Exception as e:
                print(f"✗ Error al sincronizar {filename}: {e}")
    
    def _save_offline(self, tabla, json_data):
        """Guarda los datos en un archivo JSON local"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{tabla}_{timestamp}.json"
            filepath = os.path.join(self.offline_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            
            print(f"✓ Datos guardados localmente en: {filepath}")
        except Exception as e:
            print(f"✗ Error al guardar archivo local: {e}")