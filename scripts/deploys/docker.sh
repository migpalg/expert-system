CURRENT_TAG=$(git describe --tags --abbrev=0)
REQUIREMENTS_FILE=requirements.txt
python -m pipenv lock --requirements > $REQUIREMENTS_FILE
docker build -t migpalg.dev/expert/api:$CURRENT_TAG -f docker/Dockerfile .
rm $REQUIREMENTS_FILE
