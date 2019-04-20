# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: packet-sock.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opts_pb2 as opts__pb2
import fown_pb2 as fown__pb2
import sk_opts_pb2 as sk__opts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='packet-sock.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11packet-sock.proto\x1a\nopts.proto\x1a\nfown.proto\x1a\rsk-opts.proto\":\n\rpacket_mclist\x12\r\n\x05index\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\r\x12\x0c\n\x04\x61\x64\x64r\x18\x03 \x02(\x0c\"\x94\x01\n\x0bpacket_ring\x12\x12\n\nblock_size\x18\x01 \x02(\r\x12\x10\n\x08\x62lock_nr\x18\x02 \x02(\r\x12\x12\n\nframe_size\x18\x03 \x02(\r\x12\x10\n\x08\x66rame_nr\x18\x04 \x02(\r\x12\x12\n\nretire_tmo\x18\x05 \x02(\r\x12\x13\n\x0bsizeof_priv\x18\x06 \x02(\r\x12\x10\n\x08\x66\x65\x61tures\x18\x07 \x02(\r\"\xb6\x03\n\x11packet_sock_entry\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04type\x18\x02 \x02(\r\x12\x10\n\x08protocol\x18\x03 \x02(\r\x12\x14\n\x05\x66lags\x18\x04 \x02(\rB\x05\xd2?\x02\x08\x01\x12\x0f\n\x07ifindex\x18\x05 \x02(\r\x12\x19\n\x04\x66own\x18\x06 \x02(\x0b\x32\x0b.fown_entry\x12\x1c\n\x04opts\x18\x07 \x02(\x0b\x32\x0e.sk_opts_entry\x12\x0f\n\x07version\x18\x08 \x02(\r\x12\x0f\n\x07reserve\x18\t \x02(\r\x12\x10\n\x08\x61ux_data\x18\n \x02(\x08\x12\x10\n\x08orig_dev\x18\x0b \x02(\x08\x12\x10\n\x08vnet_hdr\x18\x0c \x02(\x08\x12\x0c\n\x04loss\x18\r \x02(\x08\x12\x11\n\ttimestamp\x18\x0e \x02(\r\x12\x13\n\x0b\x63opy_thresh\x18\x0f \x02(\r\x12\x1e\n\x06mclist\x18\x10 \x03(\x0b\x32\x0e.packet_mclist\x12\x1a\n\x06\x66\x61nout\x18\x11 \x01(\r:\n4294967295\x12\x1d\n\x07rx_ring\x18\x12 \x01(\x0b\x32\x0c.packet_ring\x12\x1d\n\x07tx_ring\x18\x13 \x01(\x0b\x32\x0c.packet_ring\x12\r\n\x05ns_id\x18\x14 \x01(\r')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,fown__pb2.DESCRIPTOR,sk__opts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PACKET_MCLIST = _descriptor.Descriptor(
  name='packet_mclist',
  full_name='packet_mclist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='packet_mclist.index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='packet_mclist.type', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='addr', full_name='packet_mclist.addr', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=118,
)


_PACKET_RING = _descriptor.Descriptor(
  name='packet_ring',
  full_name='packet_ring',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_size', full_name='packet_ring.block_size', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='block_nr', full_name='packet_ring.block_nr', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_size', full_name='packet_ring.frame_size', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame_nr', full_name='packet_ring.frame_nr', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retire_tmo', full_name='packet_ring.retire_tmo', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sizeof_priv', full_name='packet_ring.sizeof_priv', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='features', full_name='packet_ring.features', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=269,
)


_PACKET_SOCK_ENTRY = _descriptor.Descriptor(
  name='packet_sock_entry',
  full_name='packet_sock_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='packet_sock_entry.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='packet_sock_entry.type', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='packet_sock_entry.protocol', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='packet_sock_entry.flags', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='ifindex', full_name='packet_sock_entry.ifindex', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fown', full_name='packet_sock_entry.fown', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opts', full_name='packet_sock_entry.opts', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='packet_sock_entry.version', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reserve', full_name='packet_sock_entry.reserve', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux_data', full_name='packet_sock_entry.aux_data', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_dev', full_name='packet_sock_entry.orig_dev', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vnet_hdr', full_name='packet_sock_entry.vnet_hdr', index=11,
      number=12, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='loss', full_name='packet_sock_entry.loss', index=12,
      number=13, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='packet_sock_entry.timestamp', index=13,
      number=14, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='copy_thresh', full_name='packet_sock_entry.copy_thresh', index=14,
      number=15, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mclist', full_name='packet_sock_entry.mclist', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fanout', full_name='packet_sock_entry.fanout', index=16,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4294967295,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rx_ring', full_name='packet_sock_entry.rx_ring', index=17,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx_ring', full_name='packet_sock_entry.tx_ring', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ns_id', full_name='packet_sock_entry.ns_id', index=19,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=710,
)

_PACKET_SOCK_ENTRY.fields_by_name['fown'].message_type = fown__pb2._FOWN_ENTRY
_PACKET_SOCK_ENTRY.fields_by_name['opts'].message_type = sk__opts__pb2._SK_OPTS_ENTRY
_PACKET_SOCK_ENTRY.fields_by_name['mclist'].message_type = _PACKET_MCLIST
_PACKET_SOCK_ENTRY.fields_by_name['rx_ring'].message_type = _PACKET_RING
_PACKET_SOCK_ENTRY.fields_by_name['tx_ring'].message_type = _PACKET_RING
DESCRIPTOR.message_types_by_name['packet_mclist'] = _PACKET_MCLIST
DESCRIPTOR.message_types_by_name['packet_ring'] = _PACKET_RING
DESCRIPTOR.message_types_by_name['packet_sock_entry'] = _PACKET_SOCK_ENTRY

packet_mclist = _reflection.GeneratedProtocolMessageType('packet_mclist', (_message.Message,), dict(
  DESCRIPTOR = _PACKET_MCLIST,
  __module__ = 'packet_sock_pb2'
  # @@protoc_insertion_point(class_scope:packet_mclist)
  ))
_sym_db.RegisterMessage(packet_mclist)

packet_ring = _reflection.GeneratedProtocolMessageType('packet_ring', (_message.Message,), dict(
  DESCRIPTOR = _PACKET_RING,
  __module__ = 'packet_sock_pb2'
  # @@protoc_insertion_point(class_scope:packet_ring)
  ))
_sym_db.RegisterMessage(packet_ring)

packet_sock_entry = _reflection.GeneratedProtocolMessageType('packet_sock_entry', (_message.Message,), dict(
  DESCRIPTOR = _PACKET_SOCK_ENTRY,
  __module__ = 'packet_sock_pb2'
  # @@protoc_insertion_point(class_scope:packet_sock_entry)
  ))
_sym_db.RegisterMessage(packet_sock_entry)


_PACKET_SOCK_ENTRY.fields_by_name['flags'].has_options = True
_PACKET_SOCK_ENTRY.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
