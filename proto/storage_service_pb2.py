# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/storage_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bproto/storage_service.proto\x12\x07Storage\"&\n\x07\x45xpense\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"M\n\x0bUserExpense\x12!\n\x07\x65xpense\x18\x01 \x01(\x0b\x32\x10.Storage.Expense\x12\x1b\n\x04user\x18\x02 \x01(\x0b\x32\r.Storage.User\"%\n\x04User\x12\x0f\n\x07\x63hat_id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x1c\n\x06Status\x12\x12\n\nis_success\x18\x01 \x01(\x08\"K\n\x08\x45xpenses\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.Storage.Expense\x12\x1f\n\x06status\x18\x02 \x01(\x0b\x32\x0f.Storage.Status\"3\n\x05Money\x12\x1b\n\x04user\x18\x01 \x01(\x0b\x32\r.Storage.User\x12\r\n\x05value\x18\x02 \x01(\x02\"B\n\x10GetMoneyResponse\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x1f\n\x06status\x18\x02 \x01(\x0b\x32\x0f.Storage.Status2\xa8\x03\n\x07Storage\x12+\n\x07\x61\x64\x64User\x12\r.Storage.User\x1a\x0f.Storage.Status\"\x00\x12.\n\nremoveUser\x12\r.Storage.User\x1a\x0f.Storage.Status\"\x00\x12\x35\n\naddExpense\x12\x14.Storage.UserExpense\x1a\x0f.Storage.Status\"\x00\x12\x38\n\rremoveExpense\x12\x14.Storage.UserExpense\x1a\x0f.Storage.Status\"\x00\x12\x31\n\x0bgetExpenses\x12\r.Storage.User\x1a\x11.Storage.Expenses\"\x00\x12\x35\n\nsetExpense\x12\x14.Storage.UserExpense\x1a\x0f.Storage.Status\"\x00\x12-\n\x08\x61\x64\x64Money\x12\x0e.Storage.Money\x1a\x0f.Storage.Status\"\x00\x12\x36\n\x08getMoney\x12\r.Storage.User\x1a\x19.Storage.GetMoneyResponse\"\x00\x62\x06proto3')



_EXPENSE = DESCRIPTOR.message_types_by_name['Expense']
_USEREXPENSE = DESCRIPTOR.message_types_by_name['UserExpense']
_USER = DESCRIPTOR.message_types_by_name['User']
_STATUS = DESCRIPTOR.message_types_by_name['Status']
_EXPENSES = DESCRIPTOR.message_types_by_name['Expenses']
_MONEY = DESCRIPTOR.message_types_by_name['Money']
_GETMONEYRESPONSE = DESCRIPTOR.message_types_by_name['GetMoneyResponse']
Expense = _reflection.GeneratedProtocolMessageType('Expense', (_message.Message,), {
  'DESCRIPTOR' : _EXPENSE,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.Expense)
  })
_sym_db.RegisterMessage(Expense)

UserExpense = _reflection.GeneratedProtocolMessageType('UserExpense', (_message.Message,), {
  'DESCRIPTOR' : _USEREXPENSE,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.UserExpense)
  })
_sym_db.RegisterMessage(UserExpense)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.User)
  })
_sym_db.RegisterMessage(User)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.Status)
  })
_sym_db.RegisterMessage(Status)

Expenses = _reflection.GeneratedProtocolMessageType('Expenses', (_message.Message,), {
  'DESCRIPTOR' : _EXPENSES,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.Expenses)
  })
_sym_db.RegisterMessage(Expenses)

Money = _reflection.GeneratedProtocolMessageType('Money', (_message.Message,), {
  'DESCRIPTOR' : _MONEY,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.Money)
  })
_sym_db.RegisterMessage(Money)

GetMoneyResponse = _reflection.GeneratedProtocolMessageType('GetMoneyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMONEYRESPONSE,
  '__module__' : 'proto.storage_service_pb2'
  # @@protoc_insertion_point(class_scope:Storage.GetMoneyResponse)
  })
_sym_db.RegisterMessage(GetMoneyResponse)

_STORAGE = DESCRIPTOR.services_by_name['Storage']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXPENSE._serialized_start=40
  _EXPENSE._serialized_end=78
  _USEREXPENSE._serialized_start=80
  _USEREXPENSE._serialized_end=157
  _USER._serialized_start=159
  _USER._serialized_end=196
  _STATUS._serialized_start=198
  _STATUS._serialized_end=226
  _EXPENSES._serialized_start=228
  _EXPENSES._serialized_end=303
  _MONEY._serialized_start=305
  _MONEY._serialized_end=356
  _GETMONEYRESPONSE._serialized_start=358
  _GETMONEYRESPONSE._serialized_end=424
  _STORAGE._serialized_start=427
  _STORAGE._serialized_end=851
# @@protoc_insertion_point(module_scope)