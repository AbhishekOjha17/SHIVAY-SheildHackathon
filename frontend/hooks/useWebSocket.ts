'use client'

import { useEffect, useState } from 'react'
import { connectWebSocket, disconnectWebSocket, getSocket } from '@/lib/websocket'

export function useWebSocket() {
  const [connected, setConnected] = useState(false)
  const [messages, setMessages] = useState<any[]>([])

  useEffect(() => {
    const socket = connectWebSocket()

    socket.on('connect', () => {
      setConnected(true)
    })

    socket.on('disconnect', () => {
      setConnected(false)
    })

    socket.on('message', (data: any) => {
      setMessages((prev) => [...prev, data])
    })

    return () => {
      disconnectWebSocket()
    }
  }, [])

  const sendMessage = (channel: string, data: any) => {
    const socket = getSocket()
    if (socket) {
      socket.emit('subscribe', { type: 'subscribe', channel, data })
    }
  }

  return { connected, messages, sendMessage }
}

