module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/vue3-essential',
    '@vue/standard',
    'eslint:recommended', // X
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    semi: 0, // Makes sure that semi colons can be used.
    indent: 0, // Ignores indent mistakes.
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off'
  }
}
