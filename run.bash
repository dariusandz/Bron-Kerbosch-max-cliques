VERTICES=60
for i in {1..16}; do
  python max-clique.py r $VERTICES True 20
  VERTICES=$(($VERTICES + 5))
done