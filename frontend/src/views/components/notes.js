import React, { Component } from 'react'
import { Container } from 'semantic-ui-react'

export default class Notes extends Component {
  render() {
    return (
      <Container fluid text>
        <Transcript/>
      </Container>
    )
  }
}
