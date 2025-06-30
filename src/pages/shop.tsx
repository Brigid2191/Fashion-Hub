"use client"

import { useEffect, useState } from "react"
import { Link } from "react-router-dom"
import { useCart } from "../contexts/cart-context"
import { ShoppingCart } from "lucide-react"
import { Product } from "../services/types"

interface FashionProduct extends Product {
  photographer?: string
  photographer_url?: string
}

export function ShopPage() {
  const { addToCart } = useCart()
  const [products, setProducts] = useState<FashionProduct[]>([])

  useEffect(() => {
    const API_URL = "https://fashion-hub-backend-gvjf.onrender.com"
    fetch(`${API_URL}/api/fashion-images`)
      .then((res) => res.json())
      .then((data) => {
        const mapped = data.map((item: any) => ({
          id: item.id,
          name: item.description || "Fashion Item",
          price: Math.floor(Math.random() * 80 + 30),
          image: item.url || "/placeholder.svg",
          category: "Fashion",
          description: item.description || "Stylish fashion piece from Unsplash",
          photographer: item.photographer,
          photographer_url: item.photographer_url,
        }))
        setProducts(mapped)
      })
      .catch(console.error)
  }, [])

  function normalizeProduct(product: FashionProduct): Product {
    return {
      id: product.id,
      name: product.name,
      price: product.price,
      image: product.image || "/placeholder.svg",
      category: product.category,
      description: product.description || "Fashion product",
    }
  }

  return (
    <div className="min-h-screen p-8 bg-gray-50">
      <div className="container mx-auto">
        <h1 className="mb-8 text-3xl font-bold text-gray-800">Fashion Hub Collection</h1>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {products.map((product) => (
            <div key={product.id} className="card shadow-md rounded overflow-hidden">
              <img
                src={product.image || "/placeholder.svg"}
                alt={product.name}
                className="w-full h-48 object-cover"
              />
              <div className="p-4">
                <h3 className="font-semibold text-lg">{product.name}</h3>
                {product.photographer && (
                  <p className="text-sm text-gray-600">
                    By{" "}
                    <a
                      href={product.photographer_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="underline"
                    >
                      {product.photographer}
                    </a>
                  </p>
                )}
                <div className="flex justify-between items-center mt-4">
                  <span className="font-bold text-green-600">${product.price}</span>
                  <div className="flex gap-2">
                    <Link to={`/product/${product.id}`} className="btn btn-outline btn-sm">
                      View
                    </Link>
                    <button
                      className="btn btn-primary btn-sm flex items-center gap-1"
                      onClick={() => addToCart(normalizeProduct(product))}
                    >
                      <ShoppingCart size={16} />
                      <span>Add</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {products.length === 0 && (
          <div className="text-center p-8 text-gray-500 text-lg">Loading products...</div>
        )}
      </div>
    </div>
  )
}
