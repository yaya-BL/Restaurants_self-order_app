import React, { useState } from 'react'
import { useEffect } from 'react'
import { Dimensions, Image, Pressable, SafeAreaView, Text, TouchableOpacity, View } from 'react-native'
import IndicatorCircle from '../../components/IndicatorCircle/IndicatorCircle.component'
import styles from './Welcome.style'

const Welcome = ({navigation}) => {

    const [currentSelection, setCurrentSelection] = useState(0)

    const data = [
        {
            title: 'Place an order in the app',
            decription: 'Volutpat molestie proin turpis pretium molestie penatibus.'
        },
        {
            title: 'Track your delivery in real time',
            decription: 'Volutpat molestie proin turpis pretium molestie penatibus.'
        },
        {
            title: 'Enjoy your meal',
            decription: 'Volutpat molestie proin turpis pretium molestie penatibus.'
        }
    ]

    useEffect(()=>{
    })

    const actionButton = (reverse) => {
        if(!reverse && currentSelection < 2){
            setCurrentSelection(currentSelection+1)
        }else if(currentSelection > 0){
            setCurrentSelection(currentSelection-1)
        }else{
            //Nothing
        }
    }

    return(
        <>
            <SafeAreaView>
                <View style={[styles.container, {height: Dimensions.get('window').height}]}>
                    <View style={styles.skipButton}>
                        {
                            currentSelection < 2 && 
                                <Text style={styles.text}>Skip</Text>
                        }
                    </View>
                    <View style={styles.imageHolder}>
                        <Image style={styles.image} source={require('../../assets/images/somecircle.png')}/>
                    </View>
                    <View style={styles.body}>
                        <View>
                            <Text style={styles.title}>{data[currentSelection].title}</Text>
                        </View>
                        <View>
                            <Text style={[styles.text, styles.textCenter]}>{data[currentSelection].decription}</Text>
                        </View>
                    </View>
                    <View style={[styles.footer, currentSelection == 2 ? styles.altFooter : {}]}>
                        {
                            currentSelection == 2
                            ?
                                <View style={styles.footerContent2}>
                                    <Pressable style={styles.button}>
                                        <Text style={styles.buttonText}>Get Started</Text>
                                    </Pressable>
                                    <Pressable style={[styles.button,styles.altButton]} onPress={()=> navigation.navigate('Auth')}>
                                        <Text style={[styles.buttonText, styles.altButtonText]}>Sign In</Text>
                                    </Pressable>
                                </View>
                            :
                                <View style={styles.footerContent}>
                                    <IndicatorCircle count={3} current={currentSelection}/>
                                    
                                    <View style={styles.rightActions}>
                                        <TouchableOpacity style={styles.circleButton} onPress={()=>actionButton(true)}>

                                        </TouchableOpacity>
                                        <View style={styles.actionSpace}/>
                                        <TouchableOpacity style={styles.circleButton} onPress={()=>actionButton(false)}>

                                        </TouchableOpacity>
                                    </View>
                                </View>
                        }
                    </View>
                </View>
            </SafeAreaView>
        </>
    )
}

export default Welcome