<template>
  <div id="container">
    <div>
      <div style="position: absolute; top: 10px; left: 50px;">
        <editor id="editor" v-model="content" @init="editorInit" lang="python" theme="dracula" width="750px" height="300px"></editor>
      </div>
      <div style="position: absolute; top: 10px; left: 820px;">
        <button type="button" class="btn btn-info" v-on:click="run">RUN</button>
      </div>
    </div>
    <div style="position: absolute; top: 400px; left: 50px;">
      <editor id="output" v-model="outputContent" @init="editorRender" lang="python" theme="chaos" width="750px" height="300px"></editor>
    </div>
  </div>
</template>

<script>
import PythonAPI from './services/PythonAPI'

export default {
  name: 'HelloWorld',
  components: { editor: require('vue2-ace-editor') },
  data () {
    return {
      content: '',
      outputContent: ''
    }
  },
  methods: {
    editorInit: function (editor) {
      require('brace/mode/html')
      require('brace/mode/python')
      require('brace/mode/less')
      require('brace/ext/language_tools')
      require('brace/theme/chrome')
      require('brace/theme/dracula')
      require('brace/theme/idle_fingers')

      editor.setOption('fontSize', '16pt')
      editor.setOption('vScrollBarAlwaysVisible', true)
      editor.setOption('theme', 'ace/theme/textmate')

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
    },
    editorRender: function (output) {
      require('brace/mode/html')
      require('brace/mode/python')
      require('brace/mode/less')
      require('brace/ext/language_tools')
      require('brace/theme/chrome')
      require('brace/theme/chaos')
      require('brace/theme/idle_fingers')

      output.setOption('fontSize', '16pt')
      output.setOption('vScrollBarAlwaysVisible', true)
      output.setOption('theme', 'ace/theme/textmate')
    },
    run: function () {
      let params = {content: this.content}
      const self = this
      PythonAPI.runScript(params, (response) => {
        console.log(response)
        self.outputContent += response.data.output
      }, (error) => {
        console.log(error)
      })
    }
  },
  created: function () {
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
