# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prediction_service.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

import predict_pb2 as predict__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='prediction_service.proto',
    package='tensorflow.serving',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x18prediction_service.proto\x12\x12tensorflow.serving\x1a\rpredict.proto2g\n\x11PredictionService\x12R\n\x07Predict\x12\".tensorflow.serving.PredictRequest\x1a#.tensorflow.serving.PredictResponseB\x03\xf8\x01\x01\x62\x06proto3'),
    dependencies=[predict__pb2.DESCRIPTOR, ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('\370\001\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class PredictionServiceStub(object):
  """PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Predict = channel.unary_unary(
        '/tensorflow.serving.PredictionService/Predict',
        request_serializer=predict__pb2.PredictRequest.SerializeToString,
        response_deserializer=predict__pb2.PredictResponse.FromString, )


class PredictionServiceServicer(object):
  """PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def Predict(self, request, context):
    """Predict -- provides access to loaded TensorFlow model.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PredictionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=predict__pb2.PredictRequest.FromString,
          response_serializer=predict__pb2.PredictResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'tensorflow.serving.PredictionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler, ))


class BetaPredictionServiceServicer(object):
  """PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def Predict(self, request, context):
    """Predict -- provides access to loaded TensorFlow model.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaPredictionServiceStub(object):
  """PredictionService provides access to machine-learned models loaded by
  model_servers.
  """

  def Predict(self,
              request,
              timeout,
              metadata=None,
              with_call=False,
              protocol_options=None):
    """Predict -- provides access to loaded TensorFlow model.
    """
    raise NotImplementedError()

  Predict.future = None


def beta_create_PredictionService_server(servicer,
                                         pool=None,
                                         pool_size=None,
                                         default_timeout=None,
                                         maximum_timeout=None):
  request_deserializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
      predict__pb2.PredictRequest.FromString,
  }
  response_serializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
      predict__pb2.PredictResponse.SerializeToString,
  }
  method_implementations = {
      ('tensorflow.serving.PredictionService', 'Predict'):
      face_utilities.unary_unary_inline(servicer.Predict),
  }
  server_options = beta_implementations.server_options(
      request_deserializers=request_deserializers,
      response_serializers=response_serializers,
      thread_pool=pool,
      thread_pool_size=pool_size,
      default_timeout=default_timeout,
      maximum_timeout=maximum_timeout)
  return beta_implementations.server(
      method_implementations, options=server_options)


def beta_create_PredictionService_stub(channel,
                                       host=None,
                                       metadata_transformer=None,
                                       pool=None,
                                       pool_size=None):
  request_serializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
      predict__pb2.PredictRequest.SerializeToString,
  }
  response_deserializers = {
      ('tensorflow.serving.PredictionService', 'Predict'):
      predict__pb2.PredictResponse.FromString,
  }
  cardinalities = {'Predict': cardinality.Cardinality.UNARY_UNARY, }
  stub_options = beta_implementations.stub_options(
      host=host,
      metadata_transformer=metadata_transformer,
      request_serializers=request_serializers,
      response_deserializers=response_deserializers,
      thread_pool=pool,
      thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(
      channel,
      'tensorflow.serving.PredictionService',
      cardinalities,
      options=stub_options)
# @@protoc_insertion_point(module_scope)
