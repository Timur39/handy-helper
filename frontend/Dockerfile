FROM node:alpine as build

WORKDIR /frontend

COPY  package.json package.json

RUN npm install package.json

COPY . .

RUN npm run build


FROM nginx:stable-alpine


COPY --from=build /build /usr/share/nginx/html
COPY --from=build nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
CMD [ "nginx", "-g", "daemon off;" ]
