!/etc/bin/bash

echo "testing MyPoint Class"
python3 -m unittest test/mypoint_test.py
echo ""
echo "testing PointRepository Class"

python3 -m unittest test/pointrepository_test.py