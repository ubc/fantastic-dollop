FROM node:10 AS build
COPY ./ /app
WORKDIR /app
RUN yarn install
RUN yarn build --modern

FROM nginx:1.17-alpine
RUN mkdir /app
COPY --from=build /app/dist /app
COPY docker/production/nginx.conf /etc/nginx/nginx.conf
