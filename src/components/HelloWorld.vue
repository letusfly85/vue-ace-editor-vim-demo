<template>
  <div>
    <editor v-model="content" @init="editorInit" lang="python" theme="chrome" width="500" height="600" fontSize="20pt"></editor>
  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  components: { editor: require('vue2-ace-editor') },
  data () {
    return {
      content: ''
    }
  },
  methods: {
    editorInit: function (editor) {
      require('brace/mode/html')
      require('brace/mode/python')
      require('brace/mode/less')
      require('brace/ext/language_tools')
      require('brace/theme/chrome')

      editor.setOption('fontSize', '14pt')

      // https://github.com/thlorenz/brace/issues/81
      const ace = require('brace')
      require('brace/keybinding/vim')

      ace.config.loadModule('ace/keyboard/vim', module => {
        const VimApi = module.CodeMirror.Vim
        VimApi.defineEx('write', 'w', (cm, input) => {
          console.log('write')
        })
      })
      editor.setKeyboardHandler('ace/keyboard/vim')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
