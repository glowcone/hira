import React from 'react'
import { 
  Header,
  Icon,
  Image
} from 'semantic-ui-react'

const SidebarItem = (props) => (
  <div>
    <Header as='h2' icon textAlign='center'>
      <Icon name={props.icon} circular />
      <Header.Content>
        {props.name}
      </Header.Content>
    </Header>
  </div>
)

export default SidebarItem;
