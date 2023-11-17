import React from 'react';
import { View, TouchableOpacity, Text } from 'react-native';
import { MaterialIcons } from '@expo/vector-icons'; 

const LevelIconComponent = ({ level, onPress }) => {
    const unlocked = level.unlocked;
    const index = level.level_index;
    
  return (
    <View key={level.level_id} style={{ justifyContent: 'flex-end', alignItems: 'center' }}>
      <TouchableOpacity
        onPress={() => onPress(level)}
        style={{
          width: 50,
          height: 50,
          justifyContent: 'center',
          alignItems: 'center',
          marginVertical: 5,
          marginRight: 5,
          backgroundColor: unlocked ? 'lightblue' : 'gray',
          borderRadius: 25,
          shadowOffset: { width: 0, height: 0 },
          shadowRadius: 5,
          shadowOpacity: 0.8,
          elevation: 5,
          borderColor: 'black',  // Add this line to add a black border
          borderWidth: 2,       // Add this line to set the border width
        }}
      >
        {unlocked ? (
            
            <Text style={{ fontSize: 18, color: 'black',fontStyle:"italic" }}>{index}</Text>
        ) : (
            <MaterialIcons name="lock" size={24} color="black"/>
        )}


      </TouchableOpacity>
    </View>
  );
};

export default LevelIconComponent;
