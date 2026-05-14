#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec2 uv;
   
out vec3 color;
uniform mat4 modelTransformation;
uniform mat4 viewTransformation;
uniform mat4 projectionMatrix;
void main()
{
   gl_Position = vec4(0.0,0.0,0.0,1.0); // projectionMatrix * viewTransformation * modelTransformation * vec4(position, 1.0);
   color = vec3(uv, 0.0);
}