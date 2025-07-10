test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          6958307009d94c1d298ae9f450f606ff
          # locked
          >>> len(pokemon)
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          e6efc1fcfbebed28c5068a807b6cce64
          # locked
          >>> 'mewtwo' in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'pikachu' in pokemon
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 25 in pokemon
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 148 in pokemon.values()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> 151 in pokemon.keys()
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> 'mew' in pokemon.keys()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> pokemon.get(151, 170)
          37048be7f7969adc76f07575c6b89a5c
          # locked
          >>> ('mew', 25) in pokemon.items()
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          311478efa7505dcdcb0779d4d503b284
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> mystery = {i - 1: i**2 for i in range(5)}
          >>> mystery[2]
          dfe3d4127f271ed2ba8f1760d7e90e4f
          # locked
          >>> mystery[4]
          8dfecce35cfbb620490b1aa9637bdafd
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
