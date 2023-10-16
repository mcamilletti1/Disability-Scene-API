-- settings.sql
CREATE DATABASE disability_scene;
CREATE USER disability_sceneuser WITH PASSWORD 'disabilityscene';
GRANT ALL PRIVILEGES ON DATABASE disability_scene TO disability_sceneuser;