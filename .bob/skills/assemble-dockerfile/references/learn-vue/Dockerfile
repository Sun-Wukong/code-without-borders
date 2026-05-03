FROM node:latest
FROM caddy
EXPOSE 80
EXPOSE 443
WORKSPACE /vue
COPY app /vue/app
COPY Caddyfile /config
CMD [ "caddy", "run", "--config", "/config/Caddyfile"]
