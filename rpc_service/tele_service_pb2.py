# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tele_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tele_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12tele_service.proto\")\n\rempty_request\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\"\x9b\x01\n\x0egetif_response\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x35\n\x0einterface_list\x18\x02 \x03(\x0b\x32\x1d.getif_response.if_info_entry\x1a\x38\n\rif_info_entry\x12\x0f\n\x07if_name\x18\x01 \x01(\t\x12\x16\n\x0eif_description\x18\x02 \x01(\t\"Z\n\x0frun_cap_request\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x0f\n\x07if_name\x18\x02 \x01(\t\x12\x11\n\tpkt_count\x18\x03 \x01(\x03\x12\t\n\x01k\x18\x04 \x01(\x05\"@\n\x10run_cap_response\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x12\n\nis_started\x18\x02 \x01(\x08\"A\n\x11stop_cap_response\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x12\n\nis_stopped\x18\x02 \x01(\x08\"d\n\x17get_cap_status_response\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x13\n\x0bis_finished\x18\x02 \x01(\x08\x12\x1a\n\x12\x63\x61ptured_pkt_count\x18\x03 \x01(\x03\"\xdb\x01\n\x18get_topk_result_response\x12\x18\n\x10protocol_version\x18\x01 \x01(\t\x12\x13\n\x0bis_finished\x18\x02 \x01(\x08\x12\x41\n\x0ctopk_results\x18\x03 \x03(\x0b\x32+.get_topk_result_response.topk_result_entry\x1aM\n\x11topk_result_entry\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x18\n\x10\x66low_description\x18\x02 \x01(\t\x12\x12\n\nflow_count\x18\x03 \x01(\x03\x32\xa0\x02\n\x0ctele_service\x12.\n\x0bget_if_list\x12\x0e.empty_request\x1a\x0f.getif_response\x12\x32\n\x0brun_capture\x12\x10.run_cap_request\x1a\x11.run_cap_response\x12\x32\n\x0cstop_capture\x12\x0e.empty_request\x1a\x12.stop_cap_response\x12:\n\x0eget_cap_status\x12\x0e.empty_request\x1a\x18.get_cap_status_response\x12<\n\x0fget_topk_result\x12\x0e.empty_request\x1a\x19.get_topk_result_responseb\x06proto3'
)




_EMPTY_REQUEST = _descriptor.Descriptor(
  name='empty_request',
  full_name='empty_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='empty_request.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=63,
)


_GETIF_RESPONSE_IF_INFO_ENTRY = _descriptor.Descriptor(
  name='if_info_entry',
  full_name='getif_response.if_info_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='getif_response.if_info_entry.if_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_description', full_name='getif_response.if_info_entry.if_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=221,
)

_GETIF_RESPONSE = _descriptor.Descriptor(
  name='getif_response',
  full_name='getif_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='getif_response.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interface_list', full_name='getif_response.interface_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETIF_RESPONSE_IF_INFO_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=221,
)


_RUN_CAP_REQUEST = _descriptor.Descriptor(
  name='run_cap_request',
  full_name='run_cap_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='run_cap_request.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_name', full_name='run_cap_request.if_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pkt_count', full_name='run_cap_request.pkt_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='k', full_name='run_cap_request.k', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=313,
)


_RUN_CAP_RESPONSE = _descriptor.Descriptor(
  name='run_cap_response',
  full_name='run_cap_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='run_cap_response.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_started', full_name='run_cap_response.is_started', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=379,
)


_STOP_CAP_RESPONSE = _descriptor.Descriptor(
  name='stop_cap_response',
  full_name='stop_cap_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='stop_cap_response.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_stopped', full_name='stop_cap_response.is_stopped', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=381,
  serialized_end=446,
)


_GET_CAP_STATUS_RESPONSE = _descriptor.Descriptor(
  name='get_cap_status_response',
  full_name='get_cap_status_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='get_cap_status_response.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_finished', full_name='get_cap_status_response.is_finished', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='captured_pkt_count', full_name='get_cap_status_response.captured_pkt_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=448,
  serialized_end=548,
)


_GET_TOPK_RESULT_RESPONSE_TOPK_RESULT_ENTRY = _descriptor.Descriptor(
  name='topk_result_entry',
  full_name='get_topk_result_response.topk_result_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='get_topk_result_response.topk_result_entry.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow_description', full_name='get_topk_result_response.topk_result_entry.flow_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow_count', full_name='get_topk_result_response.topk_result_entry.flow_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=770,
)

_GET_TOPK_RESULT_RESPONSE = _descriptor.Descriptor(
  name='get_topk_result_response',
  full_name='get_topk_result_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol_version', full_name='get_topk_result_response.protocol_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_finished', full_name='get_topk_result_response.is_finished', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topk_results', full_name='get_topk_result_response.topk_results', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GET_TOPK_RESULT_RESPONSE_TOPK_RESULT_ENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=551,
  serialized_end=770,
)

_GETIF_RESPONSE_IF_INFO_ENTRY.containing_type = _GETIF_RESPONSE
_GETIF_RESPONSE.fields_by_name['interface_list'].message_type = _GETIF_RESPONSE_IF_INFO_ENTRY
_GET_TOPK_RESULT_RESPONSE_TOPK_RESULT_ENTRY.containing_type = _GET_TOPK_RESULT_RESPONSE
_GET_TOPK_RESULT_RESPONSE.fields_by_name['topk_results'].message_type = _GET_TOPK_RESULT_RESPONSE_TOPK_RESULT_ENTRY
DESCRIPTOR.message_types_by_name['empty_request'] = _EMPTY_REQUEST
DESCRIPTOR.message_types_by_name['getif_response'] = _GETIF_RESPONSE
DESCRIPTOR.message_types_by_name['run_cap_request'] = _RUN_CAP_REQUEST
DESCRIPTOR.message_types_by_name['run_cap_response'] = _RUN_CAP_RESPONSE
DESCRIPTOR.message_types_by_name['stop_cap_response'] = _STOP_CAP_RESPONSE
DESCRIPTOR.message_types_by_name['get_cap_status_response'] = _GET_CAP_STATUS_RESPONSE
DESCRIPTOR.message_types_by_name['get_topk_result_response'] = _GET_TOPK_RESULT_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

empty_request = _reflection.GeneratedProtocolMessageType('empty_request', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY_REQUEST,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:empty_request)
  })
_sym_db.RegisterMessage(empty_request)

getif_response = _reflection.GeneratedProtocolMessageType('getif_response', (_message.Message,), {

  'if_info_entry' : _reflection.GeneratedProtocolMessageType('if_info_entry', (_message.Message,), {
    'DESCRIPTOR' : _GETIF_RESPONSE_IF_INFO_ENTRY,
    '__module__' : 'tele_service_pb2'
    # @@protoc_insertion_point(class_scope:getif_response.if_info_entry)
    })
  ,
  'DESCRIPTOR' : _GETIF_RESPONSE,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:getif_response)
  })
_sym_db.RegisterMessage(getif_response)
_sym_db.RegisterMessage(getif_response.if_info_entry)

run_cap_request = _reflection.GeneratedProtocolMessageType('run_cap_request', (_message.Message,), {
  'DESCRIPTOR' : _RUN_CAP_REQUEST,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:run_cap_request)
  })
_sym_db.RegisterMessage(run_cap_request)

run_cap_response = _reflection.GeneratedProtocolMessageType('run_cap_response', (_message.Message,), {
  'DESCRIPTOR' : _RUN_CAP_RESPONSE,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:run_cap_response)
  })
_sym_db.RegisterMessage(run_cap_response)

stop_cap_response = _reflection.GeneratedProtocolMessageType('stop_cap_response', (_message.Message,), {
  'DESCRIPTOR' : _STOP_CAP_RESPONSE,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:stop_cap_response)
  })
_sym_db.RegisterMessage(stop_cap_response)

get_cap_status_response = _reflection.GeneratedProtocolMessageType('get_cap_status_response', (_message.Message,), {
  'DESCRIPTOR' : _GET_CAP_STATUS_RESPONSE,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:get_cap_status_response)
  })
_sym_db.RegisterMessage(get_cap_status_response)

get_topk_result_response = _reflection.GeneratedProtocolMessageType('get_topk_result_response', (_message.Message,), {

  'topk_result_entry' : _reflection.GeneratedProtocolMessageType('topk_result_entry', (_message.Message,), {
    'DESCRIPTOR' : _GET_TOPK_RESULT_RESPONSE_TOPK_RESULT_ENTRY,
    '__module__' : 'tele_service_pb2'
    # @@protoc_insertion_point(class_scope:get_topk_result_response.topk_result_entry)
    })
  ,
  'DESCRIPTOR' : _GET_TOPK_RESULT_RESPONSE,
  '__module__' : 'tele_service_pb2'
  # @@protoc_insertion_point(class_scope:get_topk_result_response)
  })
_sym_db.RegisterMessage(get_topk_result_response)
_sym_db.RegisterMessage(get_topk_result_response.topk_result_entry)



_TELE_SERVICE = _descriptor.ServiceDescriptor(
  name='tele_service',
  full_name='tele_service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=773,
  serialized_end=1061,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_if_list',
    full_name='tele_service.get_if_list',
    index=0,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_GETIF_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='run_capture',
    full_name='tele_service.run_capture',
    index=1,
    containing_service=None,
    input_type=_RUN_CAP_REQUEST,
    output_type=_RUN_CAP_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stop_capture',
    full_name='tele_service.stop_capture',
    index=2,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_STOP_CAP_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_cap_status',
    full_name='tele_service.get_cap_status',
    index=3,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_GET_CAP_STATUS_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_topk_result',
    full_name='tele_service.get_topk_result',
    index=4,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_GET_TOPK_RESULT_RESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TELE_SERVICE)

DESCRIPTOR.services_by_name['tele_service'] = _TELE_SERVICE

# @@protoc_insertion_point(module_scope)
