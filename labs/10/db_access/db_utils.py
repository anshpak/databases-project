from data_structures.stack import Stack
from sqlalchemy.orm import make_transient


class DBUtils:
    changes_stack = Stack()

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
        DBUtils.changes_stack.push(instance, 'delete', entity.__name__)
        session.delete(instance)

    @staticmethod
    def undo_last_change(session):
        instance = DBUtils.changes_stack.pop()
        if instance.kind == 'delete':
            if instance.entity == 'Employee':
                obj = instance.value
                make_transient(obj)
                make_transient(obj.contract)
                session.add(obj)
