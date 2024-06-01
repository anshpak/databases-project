class DBUtils:
    @staticmethod
    def get_entity_data(session, entity):
        query = session.query(entity)
        return query

    @staticmethod
    def add_entity_instance(session, entity):
        session.add(entity)

    @staticmethod
    def remove_entity_instance(session, entity, id_):
        query = session.query(entity)
        instance = query.filter(entity.id == id_).first()
        session.delete(instance)
