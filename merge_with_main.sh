git config user.name "Jenkins CLI"
git config user.email "example@jenkins.com"

git fetch origin
git checkout main
git merge origin/pre_production -m "merging to production"

git push origin main

git switch pre_production

echo "Back in pre_production branch"
