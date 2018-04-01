import React, { Component } from 'react'
import { Grid } from 'semantic-ui-react'
import Sidebar from './containers/sidebar'
import Transcript from './containers/transcript'

class App extends Component {
  render() {
    return (
      <Grid stackable>
        <Grid.Row>
          <Grid.Column>
            <Notes/>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    )
  }
}

export default App
