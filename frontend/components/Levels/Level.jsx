import React from 'react';
import { TouchableOpacity, Text, View } from 'react-native';
import { SvgXml } from 'react-native-svg';
import lockSvg from '../Levels/imgSVG/lockSvg'; // Adjust the path as needed

const Level = ({ levelNumber, isOpen, onPress }) => (
    <TouchableOpacity
        style={styles.circleButton}
        onPress={() => onPress(levelNumber)}
    >
        {isOpen ? (
            <View style={styles.textContainer}>
                <Text style={{ color: '#111c3b' }}>Level</Text>
                <Text style={{ color: '#111c3b', fontWeight: 'bold' }}>{levelNumber}</Text>
            </View>
        ) : (
            <SvgXml
                xml={lockSvg}
                width={30}
                height={30}
            />
        )}
    </TouchableOpacity>
);

const styles = {
    circleButton: {
        width: 55,
        height: 55,
        backgroundColor: '#ffffff',
        borderRadius: 45,
        marginVertical: 10,
        justifyContent: 'center',
        alignItems: 'center',
    },
    textContainer: {
        alignItems: 'center',
    },
};

export default Level;
