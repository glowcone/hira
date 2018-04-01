import React, { Component } from 'react'
import { 
  Menu,
  Container
} from 'semantic-ui-react'
import SidebarItem from './sidebar-item'

export default class Sidebar extends Component {
  render() {
    return (
      <Menu fluid vertical inverted color="black" borderless compact>
        <SidebarItem name="Notes" icon="users" />
      </Menu>
    )
  }
}
