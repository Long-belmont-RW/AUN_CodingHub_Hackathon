// Dark mode functionality
const darkModeToggle = document.getElementById('darkModeToggle');
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');


darkModeToggle.addEventListener('click', () => {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateDarkModeButton();
});

function updateDarkModeButton() {
    const currentTheme = document.body.getAttribute('data-theme');
    darkModeToggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';
}

function addTask() {
    let taskInput = document.getElementById('task');
    let task = taskInput.value.trim();
    if (task) {
        let li = document.createElement('li');

        let checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.onchange = function() {
            if (this.checked) {
                taskText.style.textDecoration = 'line-through';
            s} else {
                taskText.style.textDecoration = 'none';
            }
        };

        let taskText = document.createElement('span');
        taskText.className = 'task-text';
        taskText.appendChild(document.createTextNode(task));
        taskText.onclick = function() {
            li.remove();
        };

        li.appendChild(checkbox);
        li.appendChild(taskText);

        document.getElementById('taskList').appendChild(li);
        taskInput.value = '';
    }
}

function removeAllTasks() {
    let taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
}

document.getElementById('task').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});