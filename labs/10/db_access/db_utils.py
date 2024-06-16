from data_structures.stack import Stack
from sqlalchemy.orm import make_transient

from models.skydiving import Employee


class DBUtils:
    changes_stack = Stack()

    @staticmethod
    def get_entity_data(session, entity):
        query = session.query(entity)
        return query

    @staticmethod
    def add_entity_instance(session, instance):
        DBUtils.changes_stack.push(instance, 'add', type(instance).__name__)
        session.add(instance)

    @staticmethod
    def remove_entity_instance(session, query, entity, id_):
        instance = query.filter(entity.id == id_).first()
        DBUtils.changes_stack.push(instance, 'delete', entity.__name__)
        session.delete(instance)

    @staticmethod
    def undo_last_change(session):
        node = DBUtils.changes_stack.pop()
        if node.action == 'delete':
            if node.entity == 'Employee':
                instance = node.value
                make_transient(instance)
                if instance.contract is not None:
                    make_transient(instance.contract)
                session.add(instance)
            elif node.entity == 'MaleStud':
                instance = node.value
                make_transient(instance)
                if instance.military_service is not None:
                    make_transient(instance.military_service)
                if instance.friends is not None:
                    make_transient(instance.friends)
                session.add(instance)
        if node.action == 'add':
            if node.entity == 'Employee':
                instance = node.value
                session.delete(instance)
            elif node.entity == 'MaleStud':
                instance = node.value
                session.delete(instance)
