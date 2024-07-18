const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');


function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true
    }
  });

  mainWindow.loadURL('http://localhost:8000/'); // Load the root URL

  // Open DevTools - Optional
  // mainWindow.webContents.openDevTools();

  mainWindow.on('closed', () => {
  });
}


app.on('ready', () => {
  const projectPath = '/home/jeeva/Desktop/project_me';
  const pythonExecutable = `${projectPath}/myenv/bin/python`;
  const managePyPath = `${projectPath}/manage.py`;

  const activateAndRunServer = `
    cd ${projectPath} &&
    . myenv/bin/activate &&
    ${pythonExecutable} ${managePyPath} runserver
  `;

  const djangoServer = exec(`bash -c "${activateAndRunServer}"`, { cwd: projectPath });

  djangoServer.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  djangoServer.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  djangoServer.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });

  // Wait for the Django server to start before creating the window
  setTimeout(createWindow, 5000); // Adjust the timeout as needed
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
