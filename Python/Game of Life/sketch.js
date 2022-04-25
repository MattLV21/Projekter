// make grid function
function make2DArray(cols, rows) {
  let arr = new Array(cols);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = new Array(rows);
  }
  // return grid som array
  return arr;
}

let grid;
let cols;
let rows;
let resolution = 5;

function setup() {
  createCanvas(500, 500);
  // antal cols = brede / resolution
  // antal rows = height / resolution
  cols = width / resolution;
  rows = height / resolution;
  // lave grid ud fra cols og rows
  grid = make2DArray(cols, rows);

  // giv vær celle en værdi (0 eller 1)
  for(let i = 0; i < cols; i++) {
    for(let j = 0; j < rows; j++) {
      grid[i][j] = floor(random(2));
    }
  }

  const fileSelector = document.getElementById('file');
  fileSelector.addEventListener('change', (event) => {
  //   const fileList = event.target.files;
    console.log("Not implemented yet!");
  //   const reader = new FileReader();
  //   console.log(event.target.files[0]);
  //   console.log(reader.readAsDataURL(fileList[0]))
  //   // console.log(fileList);
  });

}
function draw() {
  background(0);

  // vis alle rects som er levene
  for(let i = 0; i < cols; i++) {
    for(let j = 0; j < rows; j++) {
      let x = i * resolution;
      let y = j * resolution;

      if(grid[i][j] == 1) {
        fill(255);
        stroke(0);
        rect(x, y, resolution - 1, resolution - 1); 
      }
    }
  }
  let next = make2DArray(cols, rows);

  // Compute next based on grid
  for(let i = 0; i < cols; i++) {
    for(let j = 0; j < rows; j++) {
      let state = grid[i][j];
      // Count live neighbors!
      let neighbors = countNeighbors(grid, i, j);

      // hvis den er død og har 3 neighbors så genopliv
      if(state == 0 && neighbors == 3) {
        next[i][j] = 1;          
      } // ellers hvis den er levene og har mindre end 2 eller mere end 3 neighbors så dø
      else if(state == 1 && (neighbors < 2 || neighbors > 3)) {
        next[i][j] = 0;
      } 
      else { // elser forblive
        next[i][j] = state;
      }
    }
  }
  grid = next;
}

// tæller antal neighbors
function countNeighbors(grid, x, y) {
  let sum = 0
  for(let i = -1; i < 2; i++) {
    for(let j = -1; j < 2; j++) {
      // hvorfor idk
      let col = (x + i + cols) % cols;
      let row = (y + j + rows) % rows; 
      sum += grid[col][row];
    }
  }
  sum -= grid[x][y];
  return sum;
}

// save et table af levene og døde lifes
function TableSave() {
  grid[grid.length] = "(" + resolution + ")";
  let message = grid;
  save(message, "Game_of_Life_Grid.txt");
}
