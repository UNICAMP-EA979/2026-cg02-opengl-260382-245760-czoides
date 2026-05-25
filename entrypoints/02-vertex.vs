#version 330 core

// Utilize como base o 01-vertex.vs
// Adicione o input da UV na location=1, e crie uma nova saída para fornecer a UV ao fragment

// SEU CÓDIGO AQUI //////////////////////////////////////////////////////////////////////////

// Recebe a position no location = 0
// e as uniforms mat4 modelTransformation, viewTransformation e projectionMatrix
// 
// Converte a position para o clip space usando as transformações e armazena em gl_Position.

// SEU CÓDIGO AQUI //////////////////////////////////////////////////////////////////////////
layout (location = 0) in vec3 position;
layout (location = 1) in vec2 uv_v;

out vec3 color;
out vec2 uv;
uniform mat4 projectionMatrix;
uniform mat4 modelTransformation;
uniform mat4 viewTransformation;
void main()
{
   // projectionMatrix *  viewTransformation * modelTransformation *
   //
   gl_Position = projectionMatrix * viewTransformation * modelTransformation * vec4(position, 1.0);
   color = vec3(position.z, position.z, position.z);
   uv = uv_v;
}

/////////////////////////////////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////////////////////////////////