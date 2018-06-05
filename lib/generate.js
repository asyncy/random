function boolean() {
  return Math.random() >= 0.5;
}

function string(length) {
  let text = '';
  const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  for (let i = 0; i < length; i += 1) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
}

function integer(low, high) {
  return Math.floor(Math.random() * (high - low + 1)) + parseInt(low);
}

function list(type, length, string_length, integer_low, integer_high) {
  switch (type) {
    case 'boolean':
      return list_help(length, boolean);
    case 'string':
      return list_help(length, string, [string_length]);
    case 'integer':
      return list_help(length, integer, [integer_low, integer_high]);
  }
}

function list_help(length, fn, args) {
  const list = [];
  for (let i = 0; i < length; i += 1) {
    list.push(fn.apply(null, args));
  }
  return list;
}

module.exports = {
  boolean,
  string,
  integer,
  list,
};
