class Lista:
    def __init__(self):
        self.lista = []
        self.es_lista = True
        self.ruta = None

    #convertir a dicionario el objeto o los atributos de la lista
    def convertir_a_diccionario(self):
        if self.lista:
            return [vars(item) for item in self.lista]
        else:
            return vars(self)

    def mostrar(self):
        if self.lista:
            print("Numero de Items:" + str(len(self.lista)))
        else:
            for atributo, valor in vars(self).items():
                if not atributo.startswith("__") and atributo != "es_lista" and atributo != "lista":
                    if hasattr(valor, "__str__"):
                        print(f"{atributo}: {valor}")
                    else:
                        print(f"{atributo}: {valor}")

    def mostrar_uno(self, id):
        if self.es_lista:
            for item in self.lista:
                if item.id == id:
                    return item
        return False

    def agregar(self, data):
        if self.es_lista:
            self.mostrar_uno(data.id)
            if self.mostrar_uno(data.id):
                return False
            self.lista.append(data)
            return True
        else:
            return False

    def eliminar(self, id):
        if self.es_lista:
            for i, item in enumerate(self.lista):
                if item.id == id:
                    del self.lista[i]
                    return True
        return False

    def editar(self, sended_id, data):
        if self.es_lista:
            for item in self.lista:
                if item.id == sended_id:
                    for key, value in vars(data).items():
                        if hasattr(item, key):
                            if value != "" and value is not None:
                                setattr(item, key, value)
                    return True
        return False

    def exportar(self, ruta=None):
        if ruta:
            self.ruta = ruta

        if self.ruta is None and ruta is None:
            return False

        with open(self.ruta, 'w') as file:
            import json
            json.dump(self.convertir_a_diccionario(), file, indent=4)
        return True


    def convertir_json_objeto(self, data):
        if self.es_lista:
            self.lista = []
            for item in data:
                if 'lista' in item:
                    del item['lista']
                if 'es_lista' in item:
                    del item['es_lista']
                self.lista.append(self.__class__(**item))
        else:
            for key, value in data.items():
                if key == 'lista' or key == 'es_lista':
                    continue
                setattr(self, key, value)
        return True


    def importar(self, ruta=None):
        if ruta:
            self.ruta = ruta

        if self.ruta is None and ruta is None:
            raise ValueError("Debe proporcionar una ruta para importar el archivo JSON.")

        with open(self.ruta, 'r') as file:
            import json
            data = json.load(file)

            return self.convertir_json_objeto(data)
