"use client"

import React, { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { ShoppingBag, Star, Truck, Shield } from "lucide-react"
import api from "../services/api"

export function HomePage() {
  const [, setProducts] = useState([])

  useEffect(() => {
    api.get("/products")
      .then((res) => {
        console.log("✅ Connected to backend. Products:", res.data)
        setProducts(res.data)
      })
      .catch((err) => {
        console.error("❌ Backend connection failed:", err.message)
      })
  }, [])

  const features = [
    {
      icon: <ShoppingBag className="h-8 w-8" style={{ color: "var(--color-grey-600)" }} />,
      title: "Wide Selection",
      description: "Thousands of products across multiple categories",
    },
    {
      icon: <Star className="h-8 w-8" style={{ color: "var(--color-grey-600)" }} />,
      title: "Quality Products",
      description: "Only the best products from trusted brands",
    },
    {
      icon: <Truck className="h-8 w-8" style={{ color: "var(--color-grey-600)" }} />,
      title: "Fast Delivery",
      description: "Quick and reliable shipping to your doorstep",
    },
    {
      icon: <Shield className="h-8 w-8" style={{ color: "var(--color-grey-600)" }} />,
      title: "Secure Shopping",
      description: "Your data and payments are always protected",
    },
  ]

  return (
    <div className="min-h-screen" style={{ backgroundColor: "var(--color-grey-50)" }}>
      <section className="hero">
        <div className="container">
          <h1 className="hero-title">Welcome to ShopApp</h1>
          <p className="hero-subtitle">
            Discover amazing products at unbeatable prices. Your one-stop shop for everything you need.
          </p>
          <Link to="/shop" className="btn btn-secondary btn-lg">
            Start Shopping
          </Link>
        </div>
      </section>

      <section className="p-8">
        <div className="container">
          <h2 className="text-center mb-8 text-2xl font-bold text-gray-800">Why Choose Us?</h2>
          <div className="product-grid">
            {features.map((feature, index) => (
              <div key={index} className="card text-center">
                <div className="card-content">
                  <div className="flex justify-center mb-4">{feature.icon}</div>
                  <h3 className="card-title">{feature.title}</h3>
                  <p className="card-description">{feature.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="p-8 bg-gray-100">
        <div className="container text-center">
          <h2 className="mb-6 text-2xl font-bold text-gray-800">Ready to Start Shopping?</h2>
          <p className="mb-8 text-lg text-gray-600">
            Join thousands of satisfied customers and discover your next favorite product today.
          </p>
          <div className="flex justify-center gap-4">
            <Link to="/shop" className="btn btn-primary btn-lg">
              Browse Products
            </Link>
            <Link to="/register" className="btn btn-outline btn-lg">
              Create Account
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
