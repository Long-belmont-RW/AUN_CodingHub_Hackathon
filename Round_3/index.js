// Random password generator

function genPassword(
  passwordLength,
  includeLower,
  includeUpper,
  includeNum,
  includeSym
) {
  const lowerCaseChars = "abcdefghijklmnopqrstuvwxyz";
  const upperCaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const symbols = "!@#$%^&*+";
  const num = "0123456789";

  let allowedChars = "";
  let password = "";

  allowedChars += includeLower ? lowerCaseChars : "";
  allowedChars += includeUpper ? upperCaseChars : "";
  allowedChars += includeNum ? num : "";
  allowedChars += includeSym ? symbols : "";

  if (passwordLength <= 0) {
    return `Password length must be at least one`;
  }

  if (allowedChars.length === 0) {
    return `At least one set of characters needs to be selected`;
  }

  for (let i = 0; i < passwordLength; i++) {
    const randomIndex = Math.floor(Math.random() * allowedChars.length);
    password += allowedChars[randomIndex];
  }

  return password;
}

const passwordLength = 12;
const includeLower = true;
const includeUpper = true;
const includeNum = true;
const includeSym = true;

const password = genPassword(
  passwordLength,
  includeLower,
  includeUpper,
  includeNum,
  includeSym
);

console.log(`Generated Password: ${password}`);
