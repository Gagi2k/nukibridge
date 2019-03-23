# Copyright 2013 Donald Stufft and individual contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

import nacl.bindings
import nacl.encoding


def sha256(message, encoder=nacl.encoding.HexEncoder):
    return encoder.encode(nacl.bindings.crypto_hash_sha256(message))


def sha512(message, encoder=nacl.encoding.HexEncoder):
    return encoder.encode(nacl.bindings.crypto_hash_sha512(message))


def hmacsha256(message, k, encoder=nacl.encoding.HexEncoder):
    return encoder.encode(nacl.bindings.crypto_auth_hmacsha256(message, k))

    
def hmacsha256_verify(message, k, encoder=nacl.encoding.HexEncoder):
    return encoder.encode(nacl.bindings.crypto_auth_hmacsha256_verify(message, k))