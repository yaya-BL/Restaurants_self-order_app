import React from 'react'
import { Pressable, Text, TextInput, View } from 'react-native'
import styles from './SignIn.style'

const SignIn = ({}) => {
    return(
        <>
            <View style={styles.container}>
                <Text style={styles.title}>Welcome back!</Text>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Email</Text>
                    <TextInput style={styles.textForm} placeholder='Your email address' placeholderTextColor='#33333350'/>
                </View>
                <View style={styles.formContainer}>
                    <Text style={styles.formLabel}>Password</Text>
                    <TextInput style={styles.textForm} placeholder='Your password' placeholderTextColor='#33333350'/>
                </View>
                <View style={styles.footerTextContainer}>
                    <Text style={styles.footerText}>Forgot Password?</Text>
                </View>
                <Pressable style={styles.actionButton}>
                    <Text style={styles.actionText}>Login</Text>
                </Pressable>
            </View>
        </>
    )
}

export default SignIn;