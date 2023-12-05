# Commands Git BASH inside repository folder

# version definition
VERSION="v1.0.0"

git pull origin master
git archive --format tar.gz -o ./archive/pybioportal-"$VERSION".tar.gz "$VERSION":pybioportal/
git add .
git commit -m "Create new archive $VERSION"
git push origin master
