import React from 'react'
import { useEffect } from 'react'
import { Dimensions, Image, SafeAreaView, Text, View } from 'react-native'
import styles from './IndicatorCircle.style'
import { SvgXml } from 'react-native-svg';
import Ellipse from '../../assets/images/ellipse.svg';

const IndicatorCircle = ({count, current}) => {

    return(
        <>
            <View style={styles.ellipseContainer}>
                {
                    Array(count - 1 + 1).fill().map((value, key)=>
                        <SvgXml key={key} width="11" height="11" xml={Ellipse} fill={current == key ? '#33CCFF' : '#33CCFF60'} style={styles.ellipse}/>
                    )
                }
            </View>
        </>
    )
}

export default IndicatorCircle