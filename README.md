# Trifolium project blog

Forked from [TheAbhijeet/Django_blog](https://github.com/TheAbhijeet/Django_blog)

## Usage

**Under construction**

docker-compose logs -f -t

docker-compose down -v && docker-compose up -d --build

docker-compose -f docker-compose.prod.yml up -d 


docker-compose -f docker-compose.prod.yml up -d --build

echo $(htpasswd -nb login password) | sed -e s/\\$/\\$\\$/g