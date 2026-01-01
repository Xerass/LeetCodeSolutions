import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
#    res = person.merge(address, on = 'personId', how = 'left')

 #   print(res.columns)

  #  return res[['firstName', 'lastName', 'city', 'state']]

  #a faster solution would be to make the personID an index, probably not a good idea in the real world but is faster, slightly.

  person.set_index('personId', inplace = True)
  address.set_index('personId', inplace = True)

  #join them on said indices
  res = person.join(address, how = 'left')

  return res[['firstName', 'lastName', 'city', 'state']]
