# Trifólium project blog

Forked from [TheAbhijeet/Django_blog](https://github.com/TheAbhijeet/Django_blog)

Repository for storing website code of [Trifólium Project](https://trifolium-project.com/)

## Usage

**Under construction**

docker-compose logs -f -t

docker-compose down -v && docker-compose up -d --build

docker-compose -f docker-compose.prod.yml up -d 


docker-compose -f docker-compose.prod.yml up -d --build

echo $(htpasswd -nb login password) | sed -e s/\\$/\\$\\$/g