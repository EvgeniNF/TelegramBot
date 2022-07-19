import decimal

from proto import storage_service_pb2 as pb2
from proto import storage_service_pb2_grpc as pb2_grpc
import grpc


class Storage(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.StorageStub(self.channel)

    def addNewUser(self, chat_id, name) -> bool:
        message = pb2.User(name=name, chat_id=chat_id)
        result = self.stub.addUser(message)
        return result.is_success

    def removeUser(self, chat_id, name) -> bool:
        message = pb2.User(name=name, chat_id=chat_id)
        result = self.stub.removeUser(message)
        return result.is_success

    def addNewExpense(self, chat_id, name, expense) -> bool:
        exist_expenses = self.getNamesExpenses(chat_id, name)

        if expense in exist_expenses.keys():
            return False

        message = pb2.UserExpense(user=pb2.User(chat_id=chat_id, name=name),
                                  expense=pb2.Expense(name=expense, value=0.0))
        result = self.stub.addExpense(message)
        return result.is_success

    def removeExpense(self, chat_id, name, expense) -> bool:
        message = pb2.UserExpense(user=pb2.User(chat_id=chat_id, name=name),
                                  expense=pb2.Expense(name=expense))
        response = self.stub.removeExpense(message)
        return response.is_success

    def getNamesExpenses(self, chat_id: int, user_name: str) -> [None, dict]:
        message = pb2.User(name=user_name, chat_id=chat_id)
        response = self.stub.getExpenses(message)

        result = None

        if response.status.is_success:
            result = {}
            for value in response.data:
                result[value.name] = value.value
        return result

    def addValueExpense(self, chat_id: int, user_name: str, expense: str, value: float) -> bool:
        message = pb2.UserExpense(user=pb2.User(name=user_name, chat_id=chat_id),
                                  expense=pb2.Expense(name=expense, value=value))
        response = self.stub.setExpense(message)
        if not response.is_success:
            return False

        message = pb2.Money(user=pb2.User(chat_id=chat_id, name=user_name), value=(value * -1))
        response = self.stub.addMoney(message)

        return response.is_success

    def clearValueExpense(self, chat_id: int, user_name: str, expense: str):
        message = pb2.UserExpense(user=pb2.User(name=user_name, chat_id=chat_id),
                                  expense=pb2.Expense(name=expense, value=0.0))
        response = self.stub.setExpense(message)
        return response.is_success

    def addValueBalance(self, chat_id: int, user_name: str, value: float) -> bool:
        message = pb2.Money(user=pb2.User(chat_id=chat_id, name=user_name),
                            value=value)
        response = self.stub.addMoney(message)
        return response.is_success

    def getMoney(self, chat_id: int, user_name: str) -> [decimal.Decimal, None]:
        message = pb2.User(chat_id=chat_id, name=user_name)
        response = self.stub.getMoney(message)

        if response.status.is_success:
            return decimal.Decimal(str(round(response.value, 2)))
        return None
