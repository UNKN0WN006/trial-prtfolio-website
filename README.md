# Spaceship Portfolio Website - Phase 1: Core Scene Setup and Exploration

This README outlines the steps and code for Phase 1 of developing a 3D spaceship portfolio website using Three.js. This phase focuses on setting up the development environment and creating a basic Three.js scene.

## Project Overview

This project aims to create an immersive and engaging 3D portfolio website with a spaceship theme.  Phase 1 lays the foundation by establishing the core scene and exploring basic Three.js functionalities.

## Phase 1 Goals

* Set up the development environment.
* Create a basic Three.js scene with a simple object (e.g., a rotating cube).
* Explore Three.js examples to understand core concepts.
* Initialize a Git repository for version control.

## Development Environment Setup

1. **Project Directory:** Create a new folder named `spaceship-portfolio`.

2. **HTML File (`index.html`):** Create `index.html` in the project directory with the following content:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Spaceship Portfolio</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="[https://cdn.jsdelivr.net/npm/three@latest/build/three.min.js](https://cdn.jsdelivr.net/npm/three@latest/build/three.min.js)"></script>
    <script src="[https://cdn.jsdelivr.net/npm/three@latest/examples/js/loaders/GLTFLoader.js](https://cdn.jsdelivr.net/npm/three@latest/examples/js/loaders/GLTFLoader.js)"></script>
    <script src="script.js"></script>
</body>
</html>
```
3. **JavaScript File (script.js):** Create `script.js` in the project directory and add the following code:

4. ```javascript
   // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Light
    const light = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(light);
    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionalLight.position.set(3, 3, 3);
    scene.add(directionalLight);

    // Cube (Placeholder Object)
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshStandardMaterial({ color: 0x00ff00 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    // Camera Position
    camera.position.z = 3;

    // Animation Loop
    function animate() {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
    }

    animate();

    // Window Resize Handling
    window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
    });
   ```
# Running the Code
1. Save `index.html` and `script.js`.
2. Open `index.html` in your web browser. You should see a rotating green cube.

# Exploring Three.js Examples
Visit the official `Three.js` examples page: **https://threejs.org/examples/**
Explore the examples to learn about different `Three.js` features and concepts.

## Version Control (Git)
1. *Initialize Git:* Open a terminal in your project directory and run:
   ```bash
   git init
   ```
2. *Add and commit:*
   ```bash
   git add .
   git commit -m "Initial commit: Basic scene setup"
   ```
## Next Steps
After completing Phase 1, you can proceed to Phase 2, which involves integrating the spaceship model into the scene.

## Deliverables
* Working `index.html` and `script.js` files.
* A basic understanding of `Three.js` concepts.
* A Git repository with the project files.

