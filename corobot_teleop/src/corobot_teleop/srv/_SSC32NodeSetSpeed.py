"""autogenerated by genpy from corobot_teleop/SSC32NodeSetSpeedRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SSC32NodeSetSpeedRequest(genpy.Message):
  _md5sum = "3d4471636f3bce3a963b0d137b991728"
  _type = "corobot_teleop/SSC32NodeSetSpeedRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 left_speed
int32 right_speed
int32 speed

"""
  __slots__ = ['left_speed','right_speed','speed']
  _slot_types = ['int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       left_speed,right_speed,speed

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SSC32NodeSetSpeedRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.left_speed is None:
        self.left_speed = 0
      if self.right_speed is None:
        self.right_speed = 0
      if self.speed is None:
        self.speed = 0
    else:
      self.left_speed = 0
      self.right_speed = 0
      self.speed = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3i.pack(_x.left_speed, _x.right_speed, _x.speed))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left_speed, _x.right_speed, _x.speed,) = _struct_3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3i.pack(_x.left_speed, _x.right_speed, _x.speed))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.left_speed, _x.right_speed, _x.speed,) = _struct_3i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3i = struct.Struct("<3i")
"""autogenerated by genpy from corobot_teleop/SSC32NodeSetSpeedResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SSC32NodeSetSpeedResponse(genpy.Message):
  _md5sum = "3cd2452a26f7d8a04682f2fead8013cf"
  _type = "corobot_teleop/SSC32NodeSetSpeedResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 err


"""
  __slots__ = ['err']
  _slot_types = ['int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       err

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SSC32NodeSetSpeedResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.err is None:
        self.err = 0
    else:
      self.err = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_struct_b.pack(self.err))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.err,) = _struct_b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_struct_b.pack(self.err))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.err,) = _struct_b.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_b = struct.Struct("<b")
class SSC32NodeSetSpeed(object):
  _type          = 'corobot_teleop/SSC32NodeSetSpeed'
  _md5sum = '2fe63a67ce67826c10f43b07d0dba9cb'
  _request_class  = SSC32NodeSetSpeedRequest
  _response_class = SSC32NodeSetSpeedResponse
