// MainScreen.jsx
import React from 'react';
import { View, Text, Button,StyleSheet } from 'react-native';


  const LevelsHeader = ({ userName, currentLevel, onLogoutPress }) => {
    return (
      <View style={stylesHeader.headerContainer}>
        <View style={stylesHeader.userInfoContainer}>
          <Text style={stylesHeader.userInfoText}>{`User: ${userName}`}</Text>
          <Text style={stylesHeader.userInfoText}>{`Current Level: ${currentLevel + 1}`}</Text>
        </View>
        <Button title="Logout" onPress={onLogoutPress} />
      </View>
    );
  };
  const stylesHeader = StyleSheet.create({
    headerContainer: {
      flexDirection: 'row',
      width: '100%',
      justifyContent: 'space-between',
      alignItems: 'center',
        marginTop:20,
    //   padding: 10,
      backgroundColor: 'lightblue',
      marginBottom:20,
      
    },
    userInfoContainer: {
      
    },
    userInfoText: {
      fontSize: 14,
      fontWeight: 'bold',
      marginLeft:100,
    },
  });

export default LevelsHeader;