test = {
  'name': 'Lists, Sequences, and Mutation WWPD',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = [7//3, 5, [4, 0, 1], 2]
          >>> s[0]
          61b793952531daad90d65377b695da99
          # locked
          >>> s[2]
          176f11e2ea330c098313db1f1576967f
          # locked
          >>> s[-1]
          61b793952531daad90d65377b695da99
          # locked
          >>> len(s)
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> 4 in s
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 4 in s[2]
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> s[2] + [3 + 2]
          155bdce448ea76d920b83d1dcf697d0e
          # locked
          >>> 5 in s[2]
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> s[2] * 2
          2ada3a8823635a1d6945f06fab16565d
          # locked
          >>> list(range(3, 6))
          ac7755cdf1ff110634a6d34c9ed8e5cd
          # locked
          >>> range(3, 6)
          8c6f6a2daaf343333ab8c3e4e827dbd2
          # locked
          >>> r = range(3, 6)
          >>> [r[0], r[2]]
          b48590a202f87b02895e3dd9fb48724b
          # locked
          >>> range(4)[-1]
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> [2 * x for x in range(4)]
          b229bd0b8a172dba23d43ab250b5d467
          # locked
          >>> [y for y in [6, 1, 6, 1] if y > 2]
          6793d04e381e15e7ba73005148971b12
          # locked
          >>> [[1] + s for s in [[4], [5, 6]]]
          174a09d3332543f8cec01a14eaa0adc7
          # locked
          >>> [z + 1 for z in range(10) if z % 3 == 0]
          3a50827c745626ee1922eafb36a051ff
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> # If nothing would be output by Python, type Nothing
          >>> # If the code would error, type Error
          >>> s = [6, 7, 8]
          >>> print(s.append(6))
          cdbde137f4c79f7218e099b3e3fd6d61
          # locked
          >>> s
          8d9e529b894fd2b877505f920fc8bf10
          # locked
          >>> s.insert(0, 9)
          >>> s
          96a9523c6650d0e68d337b7802845c31
          # locked
          >>> x = s.pop(1)
          >>> s
          23d955964a41ae46ce7f5baf2e625185
          # locked
          >>> s.remove(x)
          >>> s
          74b75113b4b127b8ed39459437040eda
          # locked
          >>> a, b = s, s[:]
          >>> a is s
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b == s
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> b is s
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> a.pop()
          a78f9116f634421eb2a6b7d7c5fc74dd
          # locked
          >>> a + b
          fdd67a5c26d3c44431c707c12783f588
          # locked
          >>> s = [3]
          >>> s.extend([4, 5])
          >>> s
          ac7755cdf1ff110634a6d34c9ed8e5cd
          # locked
          >>> a
          02d6cfc29e6587caf27d88a197157c47
          # locked
          >>> s.extend([s.append(9), s.append(10)])
          >>> s
          451278ee3a935bb234a372081ae48f88
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
