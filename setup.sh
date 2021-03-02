
if [ "$1" == "" ]
then
  echo "No input file specified. Aborting."
  exit -1
fi
echo "Converting input file into JSON..."
python jsonify.py $1

if [ "$2" == "" ]
then
  port=8000
else
  port=$2
fi
echo 'Starting local server'
python3 -m http.server $port