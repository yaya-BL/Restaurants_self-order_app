import React from 'react'
import { Image, ScrollView, Text, View } from 'react-native'
import SignIn from '../../components/SignIn/SignIn.screen'
import styles from './Auth.style'

const Auth = ({}) => {
    return(
        <>
            <View style={styles.container}>
                <View style={styles.menuSliderContainer}>
                    <ScrollView contentContainerStyle={styles.dishScroll} horizontal={true} showsHorizontalScrollIndicator={false}>
                        <View style={styles.imageContainer}>
                            <Image style={styles.dishImage} source={require('../../assets/images/salad1.png')}/>
                        </View>
                        <View style={[styles.imageContainer, {paddingTop:30}]}>
                            <Image style={styles.dishImage}  source={require('../../assets/images/salad2.png')}/>
                        </View>
                    </ScrollView>
                    <View style={styles.authAbsoluteButtonContainer}>
                        <View>
                            <Text style={styles.authText}>Login</Text>
                            <View style={styles.borderButtom}/>
                        </View>
                        <View>
                            <Text style={styles.authText}>Sign-up</Text>
                            <View style={styles.borderButtom}/>
                        </View>
                    </View>
                </View>
                <SignIn/>
            </View>
        </>
    )
}

export default Auth;