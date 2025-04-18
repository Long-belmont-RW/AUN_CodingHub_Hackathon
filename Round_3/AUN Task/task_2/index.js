// Function to generate random password
function generatePassword(length, includeSymbols) {
    const lowercase = 'abcdefghijklmnopqrstuvwxyz';
    const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numbers = '0123456789';
    const symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?';
    
    let characters = lowercase + uppercase + numbers;
    if (includeSymbols) {
        characters += symbols;
    }
    
    let password = '';
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }
    
    return password;
}

// Event listener for the generate button
document.querySelector('button').addEventListener('click', function() {
    const lengthInput = document.querySelector('input[type="text"]');
    const includeSymbols = document.getElementById('includeSymbols').checked;
    const container1 = document.querySelector('.container-1');
    
    // Get password length from input
    const length = parseInt(lengthInput.value);
    
    // Validate input
    if (isNaN(length) || length <= 0) {
        container1.textContent = 'Please enter a valid password length';
        container1.style.color = 'red';
        return;
    }
    
    // Generate and display password
    const password = generatePassword(length, includeSymbols);
    container1.textContent = password;
    container1.style.color = 'black';
});
