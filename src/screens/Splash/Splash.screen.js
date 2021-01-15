import React from 'react'
import { useEffect } from 'react'
import { Text, View } from 'react-native'
import styles from './Splash.style'

const Splash = ({navigation}) => {

    useEffect(()=>{
        setTimeout(()=>{
            navigation.navigate('Welcome')
        }, 1000)
    })

    return(
        <>
            <View style={styles.container}>
                <View style={styles.childContainer}>
                    <Text style={styles.appName}>Food Order App</Text>
                </View>
                <View/>
            </View>
        </>
    )
}

export default Splash